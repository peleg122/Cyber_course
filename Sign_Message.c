#include <stdio.h>
#include <openssl/bn.h>

void printBN(char * msg, BIGNUM * a){// changes were made here for printing style
	char * number_str = BN_bn2hex(a);
	printf("%s%s", msg , number_str);
	OPENSSL_free(number_str);
}

int main(){
	BN_CTX * ctx = BN_CTX_new();
	
	BIGNUM *n = BN_new();
	BIGNUM *d = BN_new();
	BIGNUM *m = BN_new();//message
	BIGNUM *s = BN_new();//signed text

	BN_hex2bn(&n, "DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5");
	BN_hex2bn(&d, " 74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D");
	BN_hex2bn(&m, "49206f776520796f75202432303030");	

	BN_mod_exp(s, m, d, n, ctx);
	printBN("signed Message: ", s);
	printf("\n");

	return 0;
}
