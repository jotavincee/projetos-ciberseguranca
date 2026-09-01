#include <stdio.h>
#include <string.h>

void funcao_segura(void) {
    char buffer_seguro[100];

    printf("Digite uma entrada segura: ");
    
    
    if (fgets(buffer_seguro, sizeof(buffer_seguro), stdin) != NULL) {
        
        buffer_seguro[strcspn(buffer_seguro, "\n")] = '\0';
        
        printf("Dado armazenado com seguranca: %s\n", buffer_seguro);
    }
}

int main(void) {
    funcao_segura();
    return 0;
}
