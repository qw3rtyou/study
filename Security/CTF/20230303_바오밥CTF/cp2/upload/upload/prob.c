// gcc prob.c -o prob -no-pie -Wl,-z,relro,-z,now
#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>
#include <stdbool.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include "deck.h"

#define MAX_CC 313

enum ID {
    USER = 1,
    DEALER
};

enum ACTION {
    STAND = 1,
    HIT
};

typedef struct Game{
    uint32_t user;
    uint32_t dealer;
    uint32_t A_flag; 
    char card_flag[DECK];
    bool user_stand_flag;
    bool dealer_stand_flag;
    bool user_bust_flag;
    bool dealer_bust_flag;
    uint32_t coin;
} Game;

Game game;

void initialize() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    game.coin = 500;
}

static inline void init() {
    memset(&game.card_flag, 0, DECK);
    game.dealer = game.user = game.A_flag = game.user_stand_flag = game.dealer_stand_flag = game.user_bust_flag = game.dealer_bust_flag = 0;
}

uint32_t getRandom() {
    uint32_t result;
    char buf[4];
    int fd = open("/dev/urandom", O_RDONLY);
    read(fd, buf, 4);
    close(fd);
    memcpy(&result, buf, sizeof(buf));
    return result;
}

uint32_t input(const char *msg) {
    uint32_t result;
    printf("%s > ", msg);
    scanf("%d", &result);
    getchar();
    return result;
}

static inline void showWallet() {
    printf("[o] Your Coin: %d\n", game.coin);
}

static inline uint32_t getCardCode() {
    puts("[Card Code]\n"
         " Shape : ♠. 0   | ◆. 1   | ♥. 2   | ♣. 3 \n"
         " Number: A. 00  | 2. 02  | 3. 03  | 4. 04\n"
         "         5. 05  | 6. 06  | 7. 07  | 8. 08\n"
         "         9. 09  | 10. 10 | J. 11  | Q. 12\n"
         "         K. 13 \n"
         " (e.g. ♠A -> 000, ♥Q -> 212)");
    uint32_t cardcode = input("Change Card Code");
    if (cardcode < MAX_CC)     
        return (cardcode / 100 * NUMBER) + (cardcode % 100);
    return 0;
}

void chkJocker(uint32_t * card, uint32_t turn) {
    if (turn == DEALER) {
        if ((21 - game.dealer) >= 10) {
            *card = 10 * (getRandom() % (PATTERN - 1));
        } else {
            *card = (21 - game.dealer) * (getRandom() % (PATTERN - 1));
        }
    } else {
        *card = getCardCode();
    }
}

void setScore(uint32_t card, uint32_t turn) {
    int sc = card % NUMBER + 1;
    if (sc == 1) {
        if (turn == DEALER) {
            if ((game.dealer + 11) <= 21)
                sc = 11;
        } else if (turn == USER) {
            sc = 0;
            game.A_flag += 1;
        }
    } else if (sc > 10) {
        sc = 10;
    }

    if (turn == DEALER) {
        game.dealer += sc;
    } else if (turn == USER){
        game.user += sc;
    }
}

uint32_t hit(uint32_t turn) {
    uint32_t card = 0;
    while(1) {
        card = getRandom() % DECK;
        if (game.card_flag[card] > 0)
            continue;
        break;
    }
    if (card >= JOCKER) {
        showNewCard(card);
        chkJocker(&card, turn);
    }   
    game.card_flag[card] += turn;
    showNewCard(card);
    return card;
}

static inline void printScore() {
    printf("------[Score]------\n- Dealer : %d\n- User   : %d", game.dealer, game.user);
    if (game.A_flag) 
        printf(" + A Score (1 or 11)");
    puts("");
}

void printOwnCards(uint32_t turn) {
    printf("[Own Cards]\n ");
    for (int i = 0; i < DECK; i++) {
        if (game.card_flag[i] == turn || game.card_flag[i] == 3) 
            printf("%s ", deck[i]);
    }
    puts("");
}

static inline bool bustCheck() {
    if (game.dealer_bust_flag || game.user_bust_flag) {
        return 1;
    }
    return 0;
}

void chkAflag() {
    while (game.A_flag--) {
        if ((game.user + 11) > 21)
            game.user += 1;
        else 
            game.user += 11;
    }
    if (game.user > 21) 
        game.user_bust_flag = true;
}

// 비기면 돈 안돌려줌 - 악덕 사장
void endgame(uint32_t bet) {
    chkAflag();

    printf("\e[1;1H\e[2J");
    printf("==== [Game Result] ====\n- Dealer Score: %d\n- User Score: %d\n", game.dealer, game.user);
    
    if (game.dealer_bust_flag || game.user_bust_flag) {
        if (game.dealer_bust_flag && game.user_bust_flag) {
            puts("[-] Draw!");
        } else if (game.dealer_bust_flag) {
            puts("[+] Dealer Bust!! You win!");
            game.coin += bet * 2;
        } else if (game.user_bust_flag)
            puts("[-] User Bust!! You lose...");
        showWallet();
        return;
    }
    
    if (game.user == 21 || game.dealer == 21) {
        if (game.user == 21 && game.dealer == 21) {
            puts("[+] Push!");
            game.coin += bet;
        } else if (game.user == 21) {
            puts("[+] User Black Jack!! You win!");
            game.coin += bet * 2;
        } else if (game.dealer == 21) 
            puts("[-] Dealer Black Jack!! You lose...");
        showWallet();
        return;
    }

    if (game.user > game.dealer) {
        puts("[+] You win!");
        game.coin += bet * 2;
    } else if (game.user < game.dealer) {
        puts("[-] Dealer win! You lose...");
    } else {
        puts("[-] Draw!");
    }
    showWallet();
}

void blackjack() {
    init();
    showWallet();
    uint32_t card;
    uint32_t bet = input("Bet");
    
    if (bet > game.coin) 
        bet = game.coin;
    game.coin -= bet;
    
    for (int i = 0; i < 2; i++) {
        printf("\e[1;1H\e[2J");
        puts("-------- [Play Black Jack] --------");
    
        puts("[[Dealer]]");
        printOwnCards(DEALER);
        card = hit(DEALER);
        setScore(card, DEALER);
        usleep(1500000/2);

    
        puts("[[User]]");
        printOwnCards(USER);
        card = hit(USER);
        setScore(card, USER);
        usleep(1500000/2);

        printScore();
    }
    
    uint32_t dealer_act;
    uint32_t user_act;
    char *format = "[[%s - %s]]\n";
    char *player[2] = {"User", "Dealer"};
    char *action[2] = {"Stand", "Hit"};
    while (!(game.user_stand_flag && game.dealer_stand_flag)) {
        card = 0;
        dealer_act = STAND;
        user_act = STAND;
        if (game.user_stand_flag != true) {
            printf("------[Action]------\n1. Stand\n2. Hit\n");
            user_act = input("Action");
            if (user_act > 2)
                user_act = HIT; 
            if (user_act < 1) 
                user_act = STAND;
        }
        printf("\e[1;1H\e[2J");
        puts("-------- [Black Jack] --------");
        if (game.dealer <= 16) 
            dealer_act = HIT;
        else 
            dealer_act = STAND;
        printf(format, player[DEALER-1], action[dealer_act-1]);
        printOwnCards(DEALER);
        if (dealer_act == HIT) {
            card = hit(DEALER);
            setScore(card, DEALER);
            if (game.dealer > 21) 
                game.dealer_bust_flag = true;
        }
        else
            game.dealer_stand_flag = true;
        usleep(1500000/2);

        printf(format, player[USER-1], action[user_act-1]);
        printOwnCards(USER);
        if (user_act == HIT) {
            card = hit(USER);
            setScore(card, USER);
            if (game.user > 21)
                game.user_bust_flag = true;
        } else
            game.user_stand_flag = true;
        usleep(1500000/2);

        printScore();

        if (bustCheck())
            break;
    }
    endgame(bet);
    puts("[Enter]");
    getchar();
    printf("\e[1;1H\e[2J");
}

void buyFlag() {
    puts("-------- [Buy The Flag] --------");
    char flag[0x100] = {0, };
    int fd;
    if (game.coin > 1000000) {
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
    printf("\e[1;1H\e[2J");
    puts(
        "=======================================================\n"
        "\n"
        "  e88~-_       e      ,d88~~\\ 888 888b    |   ,88~-_   \n"
        " d888   \\     d8b     8888    888 |Y88b   |  d888   \\  \n"
        " 8888        /Y88b    `Y88b   888 | Y88b  | 88888    | \n"
        " 8888       /  Y88b    `Y88b, 888 |  Y88b | 88888    | \n"
        " Y888   /  /____Y88b     8888 888 |   Y88b|  Y888   /  \n"
        "  \"88_-~  /      Y88b \\__88P' 888 |    Y888   `88_-~   \n\n"
        "                    -- Black Jack --                    \n\n"
        "=======================================================\n"
    );
}

void menu() {
    puts(
        "======== [MENU] ========\n" 
        "   1. Play Black Jack   \n"
        "   2. Rule              \n"
        "   3. Buy The Flag      \n"
        "   4. Exit              \n"
        "========================"
    );
}

void rule() {
    puts(
        "-------------------------------------------------- [Rule] ---------------------------------------------------\n" 
        "   1. If your score is close to 21 points, you win. However, it must be 21 points or less. \n"
        "   2. The dealer and player are each dealt 2 cards and the game begins. \n"
        "   3. All cards are open. \n"
        "   4. You can choose whether or not to draw cards each turn. \n"
        "      If you choose Stand, you don't draw any more cards, and if you choose Hit, you draw one card. \n"
        "   5. An A card is a score of 1 or 11, which is automatically calculated in your favor at the end of the game. \n"
        "   6. When you draw a Joker, you can replace it with any card you want. \n"
        "   7. If you win the game, you get back 2x your bet. \n"
        "      However, if you draw or lose, you lose your wager. \n"
        "      (However, if you draw in blackjack, you get your wager back.) \n"
        "-----------------------------------------------------------------------------------------------------------------\n"
    );
}

int main() {
    int sel;

    initialize();
    banner();
    
    while(1) {
        menu();
        sel = input("Select");
        switch (sel) {
        case 1:
            blackjack();
            break;
        case 2:
            rule();
            break;
        case 3:
            buyFlag();
            break;
        case 4:
            return 0;
        default:
            puts("[!] Wrong Input");
            break;
        }
    }
    
    return 0;
}
