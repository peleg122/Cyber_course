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
	BIGNUM *e = BN_new();
	BIGNUM *m = BN_new();//message
	BIGNUM *c = BN_new();//ciper text

	BN_hex2bn(&n, "DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5");
	BN_hex2bn(&e, "010001");
	BN_hex2bn(&m, "4120746f702073656372657421");	

	BN_mod_exp(c, m, e, n, ctx);
	printBN("Cipher text: ",c);

	return 0;
}
