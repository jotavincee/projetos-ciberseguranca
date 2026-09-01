#include <stdio.h>
#include <string.h>

void funcao_vulneravel() {
    char buffer_inseguro[100]; 
    
    printf("Digite uma entrada segura: ");
    fgets(buffer_inseguro, sizeof(buffer_inseguro), stdin);
    
    printf("Dado armazenado com segurança: %s\n", buffer_inseguro);
}

int main() {
    funcao_vulneravel();
    return 0;
}
