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

	BN_hex2bn(&n, "AE1CD4DC432798D933779FBD46C6E1247F0CF1233595113AA51B450F18116115");
	BN_hex2bn(&e, "010001");
	BN_hex2bn(&s, "643D6F34902D9C7EC90CB0B2BCA36C47FA37165C0005CAB026C0542CBDB6802F");	

	BN_mod_exp(m, s, e, n, ctx);
	printBN("Verifyed message: ", s);
	printf("\n");

	return 0;
}
