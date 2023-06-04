// gcc -o Bank_robber Bank_robber.c -no-pie -z execstack -Wl,-z,relro,-z,now -fno-stack-protector

#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdint.h>
#include <sys/mman.h>
#include <string.h>


char vault[0x1000] = {
    0,
};

char key_table[6][10] = {"vu1nk3y", "vault1", "vault2", "unknown_key", "baobab_net", 0};

void initialize()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    mprotect(0x405000, 0x1000, PROT_EXEC|PROT_READ|PROT_WRITE);

}

// baobab ascii art src = https://emojicombos.com/baobab-ascii-art
char *baobab =
    "\033[0;32m\n"
    " \t    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
    " \t    ⠀⠀⠀⠀⠀⢠⣴⣾⣿⣿⣿⣿⣿⣶⣤⣤⣤⣶⣶⣤⣄⡀⠀⢀⣀⡀⠀⠀⠀⠀\n"
    " \t    ⠀⠀⠀⠀⢠⣿⣿⣿⣿⡿⠻⢿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣦⠀⠀⠀\n"
    " \t    ⠀⢠⣶⣿⣿⣿⡿⠛⠁⠠⣦⣠⣄⠈⠉⠉⣉⡀⠀⢀⣠⡈⠻⢿⣿⣿⡿⠀⠀⠀\n"
    " \t    ⠀⠈⠛⠛⠋⠁⠀⣚⣶⢤⣼⣿⣷⣶⣶⣾⣿⡶⢾⡛⠋⠻⠦⠄⠉⠛⠁⠀⠀⠀\n"
    " \t    ⠀⠀⠀⠀⠀⠀⠘⠋⠁⠀⠀⢹⣿⣿⣿⣿⣿⠀⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
    " \t    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
    " \t    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
    " \t    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
    " \t    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
    " \t    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
    " \t    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
    " \t    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
    " \t    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
    " \t    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⠛⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
    " ____   __    __  ____   __   ____    __ _  ____  ____ \n"
    "(  _ \\ / _\\  /  \\(  _ \\ / _\\ (  _ \\  (  ( \\(  __)(_  _)\n"
    ") _ ( /    \\(  O )) _ (/    \\ ) _ (  /    / ) _)   )(  \n"
    "(____/\\_/\\_/ \\__/(____/\\_/\\_/(____/  \\_)__)(____) (__) \n";

// bank ascii art src : https://textart.io/art/tag/bank/1
char *bank_ =
    "\033[0;0m         _._._                       _._._         \n"
    "        _|   |_                     _|   |_        \n"
    "        | ... |_._._._._._._._._._._| ... |        \n"
    "        | ||| |  o  BAOBAB BANK  o  | ||| |        \n"
    "        | \"\"\" |  \"\"\"    \"\"\"    \"\"\"  | \"\"\" |        \n"
    "   ())  |[-|-]| [-|-]  [-|-]  [-|-] |[-|-]|  ())   \n"
    "  (())) |     |---------------------|     | (()))  \n"
    " (())())| \"\"\" |  \"\"\"    \"\"\"    \"\"\"  | \"\"\" |(())()) \n"
    " (()))()|[-|-]|  :::   .-\"-.   :::  |[-|-]|(()))() \n"
    " ()))(()|     | |~|~|  |_|_|  |~|~| |     |()))(() \n"
    "    ||  |_____|_|_|_|__|_|_|__|_|_|_|_____|  ||    \n"
    " ~ ~^^ @@@@@@@@@@@@@@/=======\\@@@@@@@@@@@@@@ ^^~ ~ \n"
    "      ^~^~                                ~^~^     \n";

void clear()
{
    printf("\e[1;1H\e[2J");
}

void desc(int cash)
{
    clear();
    puts(bank_);
    printf("\033[0;0m[>] Wellcome to BAOBAB Bank!\n[>] Your current balance is %d \n[>] How can I help you? \n\t\t[1] deposit\n\t\t[2] withdraw\n\t\t[3] store\n\t\t[4] exit\n[<] ", cash);
}

void deposit(int *cash)
{
    int temp = 0;
    int deposit = *cash;
    printf("[>] Please enter the amount you wish to deposit: ");
    scanf("%d", &temp);
    deposit += temp;
    if (deposit < 0)
    {
        printf("[>] No negative numbers!");
        deposit = *cash;
    }
    *cash = deposit;
}

void withdraw(int *cash)
{
    int temp = 0;
    int withdraw = *cash;
    printf("[<] Please enter the amount you wish to withdraw: ");
    scanf("%d", &temp);
    withdraw -= temp;
    if (withdraw < 0)
    {
        printf("[>] Insufficient amount to withdraw.");
    }
    else
        *cash = withdraw;
}

void store()
{
    int addr_store = *store;
    char key[10];

    printf("[>] This is the address of the here. 0x%08lx\n", addr_store);
    int *ptr = vault;
    printf("[>] Please enter the key of the safe you want to keep.\n[<] ");
    scanf("%10s", key);
    printf("The key entered is: %s\n", key);

    if (!strcmp(key, key_table[4]))
    {
        baobab_net();
    }
    else if (!strcmp(key, key_table[0]))
    {
        printf("What would you like to keep?: ");
        read(0, ptr, 1000);
    }
    else
    {
        printf("[>] This key is not usable.\n");
        return 0;
    }
}

void leave()
{
    clear();
    printf("[>] Thank you for visiting.\n");
    exit(1);
}

void main()
{
    char buf[10] = {
        0,
    };
    int choi = 0;
    int cash = 0;

    initialize();

    while (choi != 4)
    {
        sleep(1);
        desc(cash);
        scanf("%1d", &choi);
        switch (choi)
        {
        case 1:
            deposit(&cash);
            break;
        case 2:
            withdraw(&cash);
            break;
        case 3:
            store();
            break;
        case 4:
            leave();
            break;
        }
    }
}

void baobab_net()
{
    int choi = 0;
    char buf[10] = {0,};

    while (choi != 2)
    {
        sleep(1);
        clear();
        puts(baobab);
        printf("[!] Wellcome to baobab_net for robber\n[+] vault address: 0x%08lx\n", &vault);
        printf("[1] stealing a vault\n[2] going for a robbery \n[<] ");    
        scanf("%1d", &choi);
        switch (choi)
        {
        case 1:
            read(0, buf, 23);
            break;
        case 2:
            break;
        }
    }
}