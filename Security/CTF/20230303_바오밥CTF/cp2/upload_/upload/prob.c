// gcc prob.c -o prob -no-pie -Wl,-z,relro,-z,now
#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

typedef struct {
    int coin;
    int debt_coin;
} Wallet;

Wallet wallet;

void initialize() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
}

uint64_t getRandom() {
    uint64_t result;
    char buf[8];
    int fd = open("/dev/urandom", O_RDONLY);
    read(fd, buf, 8);
    close(fd);
    memcpy(&result, buf, sizeof(buf));
    return result;
}

int input(const char *msg) {
    int result;
    printf("%s > ", msg);
    scanf("%d", &result);
    return result;
}

void showWallet() {
    printf("[+] Coin: %d\n[+] Dept Coin: %d\n",
        wallet.coin,
        wallet.debt_coin
    );
}

void spin() {
    uint32_t s_time = 50000;
    while (s_time < 500000) {
        printf(".");
        usleep(s_time);
        s_time *= 1.1;
    }
    puts("");
}

void roulette() {
    puts("-------- [Play Roulette] --------");
    printf("[+] Your Coin: %d\n", wallet.coin);
    int bet = input("Bet");
    if (wallet.coin <= 0) {
        puts("[!] You don't have coin...");
        return;
    }
    if (bet < 0 || bet > wallet.coin) {
        puts("[!] Wrong Input");
        return;
    }
    wallet.coin -= bet;
    puts("Spin!\n[Enter]");
    getchar();
    spin();
    uint64_t r = getRandom() % 10000000;
    printf("Result: ");
    if (r == 1) { 
        puts("Jackpot!!!!!\n20x!!!!");
        wallet.coin += bet * 20;
    } else if (r < 4) { 
        puts("Win!\n10x!!!");
        wallet.coin += bet * 10;
    } else if (r < 10) { 
        puts("Win!\n5x!!");
        wallet.coin += bet * 5;
    } else if (r < 9850) { 
        puts("Win!\n2x!");
        wallet.coin += bet * 2;
    } else { 
        puts("Booooom!!");
    }
    showWallet();
}

void loan() {
    puts("-------- [Loan] --------");
    int amount = input("Amount");
    if (amount < 0) {
        puts("[!] Wrong Input");
        return;
    }
    wallet.debt_coin += (amount + amount / 10);
    wallet.coin += amount;
    showWallet();
}

void payoff() {
    puts("-------- [Pay Off] --------");
    int amount = input("Amount");
    if (amount < 0 || amount > wallet.coin) {
        puts("[!] Wrong Input");
        return;
    }
    if (amount > wallet.debt_coin) {
        wallet.coin -= wallet.debt_coin;
        wallet.debt_coin = 0;
        showWallet();
        return;
    }
    wallet.debt_coin -= amount;
    wallet.coin -= amount;
    showWallet();
}

void buyFlag() {
    puts("-------- [Buy The Flag] --------");
    char flag[0x100] = {0, };
    int fd;
    if (wallet.debt_coin == 0 && wallet.coin > 100000) {
        fd = open("./flag", O_RDONLY);
        if (fd == -1) {
            puts("[!] Send DM to admin...");
            exit(0);
        }
        read(fd, flag, 0x100);
        close(fd);
        printf("Congratulations! Flag > %s\n", flag);
        exit(0);
    } else {
        puts("[+] You don't have enough coin...");
    }
}

void banner() {
    puts(
        "=======================================================\n"
        "\n"
        "  e88~-_       e      ,d88~~\\ 888 888b    |   ,88~-_   \n"
        " d888   \\     d8b     8888    888 |Y88b   |  d888   \\  \n"
        " 8888        /Y88b    `Y88b   888 | Y88b  | 88888    | \n"
        " 8888       /  Y88b    `Y88b, 888 |  Y88b | 88888    | \n"
        " Y888   /  /____Y88b     8888 888 |   Y88b|  Y888   /  \n"
        "  \"88_-~  /      Y88b \\__88P' 888 |    Y888   `88_-~   \n\n"
        "                     -- Roulette --                    \n\n"
        "=======================================================\n"
    );
}

void menu() {
    puts(
        "======== [MENU] ========\n" 
        "    1. Play Roulette    \n"
        "    2. Loan             \n"
        "    3. Pay Off          \n"
        "    4. Buy The Flag     \n"
        "    5. Exit             \n"
        "========================"
    );
}

int main() {
    int sel;

    initialize();
    banner();
    while(1) {
        menu();
        sel = input("Select");
        switch (sel)
        {
        case 1:
            roulette();
            break;
        case 2:
            loan();
            break;
        case 3:
            payoff();
            break;
        case 4:
            buyFlag();
            break;
        case 5:
            return 0;
        default:
            puts("[!] Wrong Input");
            break;
        }
    }
    
    return 0;
}
