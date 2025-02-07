#include <stdio.h>
#include <string.h>

// Fonction pour inverser une chaîne de caractères
void reverseString(char *str) {
    int n = strlen(str);
    for (int i = 0; i < n / 2; i++) {
        char temp = str[i];
        str[i] = str[n - i - 1];
        str[n - i - 1] = temp;
    }
}

int main() {
    char input[256];

    printf("Tapez quelques caractères: ");
    if (fgets(input, sizeof(input), stdin) != NULL) {
        // Supprimer le saut de ligne si présent
        size_t len = strlen(input);
        if (len > 0 && input[len - 1] == '\n') {
            input[len - 1] = '\0';
        }

        reverseString(input);
        printf("Inversion de la chaine de caractères : %s\n", input);
    } else {
        fprintf(stderr, "Error de saisie\n");
        return 1;
    }

    return 0;
}