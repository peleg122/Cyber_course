#include <stdio.h>
#include <openssl/bn.h>

void printBN(char * msg, BIGNUM * a){// changes were made here for printing style
	char * number_str = BN_bn2hex(a);
	printf("%s%s", msg , number_str);
	OPENSSL_free(number_str);
}

int main(){
	BN_CTX * ctx = BN_CTX_new();
	
	BIGNUM *i = BN_new();
	BIGNUM *p = BN_new();
	BIGNUM *pminus = BN_new();
	BIGNUM *q = BN_new();
	BIGNUM *qminus = BN_new();
	BIGNUM *n = BN_new();
	BIGNUM *d = BN_new();
	BIGNUM *e = BN_new();
	BIGNUM *piN = BN_new();

	BN_hex2bn(&p, "F7E75FDC469067FFDC4E847C51F452DF");
	BN_hex2bn(&q, "E85CED54AF57E53E092113E62F436F4F");
	BN_hex2bn(&e, "0D88C3");
	BN_dec2bn(&i, "01");

	BN_mul(n, p, q, ctx);
	printf("Public key is : ( ");printBN("", e);printBN(", ", n);
	printf(")\n");
	
	BN_sub(pminus,p,i);
	BN_sub(qminus,q,i);
	BN_mul(piN, pminus, qminus, ctx);
	BN_mod_inverse(d, e, piN, ctx);

	printf("Private key is : ( ");printBN("",d);printf(")\n");

	return 0;
}
