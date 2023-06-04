#define DECK 54
#define PATTERN 5
#define NUMBER 13
#define JOCKER 52

char * deck[DECK] = { 
    "♠A", "♠2", "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠J", "♠Q", "♠K", // 스
    "◆A", "◆2", "◆3", "◆4", "◆5", "◆6", "◆7", "◆8", "◆9", "◆10", "◆J", "◆Q", "◆K", // 다
    "♥A", "♥2", "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥J", "♥Q", "♥K", // 하
    "♣A", "♣2", "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣J", "♣Q", "♣K", // 클
    "?", "?"  // 조커
};

char * icon[] = {"♠", "◆", "♥", "♣"};

char * cA = ""
"   ------------- \n"
"  |A            |\n"
"  |O            |\n"
"  |             |\n"
"  |             |\n"
"  |      O      |\n"
"  |             |\n"
"  |             |\n"
"  |            O|\n"
"  |            A|\n"
"   ------------- \n";

char * c2 = ""
"   ------------- \n"
"  |2            |\n"
"  |O            |\n"
"  |      O      |\n"
"  |             |\n"
"  |             |\n"
"  |             |\n"
"  |      O      |\n"
"  |            O|\n"
"  |            2|\n"
"   ------------- \n";

char * c3 = ""
"   ------------- \n"
"  |3            |\n"
"  |O            |\n"
"  |      O      |\n"
"  |             |\n"
"  |      O      |\n"
"  |             |\n"
"  |      O      |\n"
"  |            O|\n"
"  |            3|\n"
"   ------------- \n";

char * c4 = ""
"   ------------- \n"
"  |4            |\n"
"  |O            |\n"
"  |   O     O   |\n"
"  |             |\n"
"  |             |\n"
"  |             |\n"
"  |   O     O   |\n"
"  |            O|\n"
"  |            4|\n"
"   ------------- \n";

char * c5 = ""
"   ------------- \n"
"  |5            |\n"
"  |O            |\n"
"  |   O     O   |\n"
"  |             |\n"
"  |      O      |\n"
"  |             |\n"
"  |   O     O   |\n"
"  |            O|\n"
"  |            5|\n"
"   ------------- \n";

char * c6 = ""
"   ------------- \n"
"  |6            |\n"
"  |O            |\n"
"  |   O     O   |\n"
"  |             |\n"
"  |   O     O   |\n"
"  |             |\n"
"  |   O     O   |\n"
"  |            O|\n"
"  |            6|\n"
"   ------------- \n";

char * c7 = ""
"   ------------- \n"
"  |7            |\n"
"  |O            |\n"
"  |   O     O   |\n"
"  |      O      |\n"
"  |   O     O   |\n"
"  |             |\n"
"  |   O     O   |\n"
"  |            O|\n"
"  |            7|\n"
"   ------------- \n";

char * c8 = ""
"   ------------- \n"
"  |8            |\n"
"  |O            |\n"
"  |   O     O   |\n"
"  |      O      |\n"
"  |   O     O   |\n"
"  |      O      |\n"
"  |   O     O   |\n"
"  |            O|\n"
"  |            8|\n"
"   ------------- \n";

char * c9 = ""
"   ------------- \n"
"  |9            |\n"
"  |O  O     O   |\n"
"  |             |\n"
"  |   O     O   |\n"
"  |      O      |\n"
"  |   O     O   |\n"
"  |             |\n"
"  |   O     O  O|\n"
"  |            9|\n"
"   ------------- \n";

char * c10 = ""
"   ------------- \n"
"  |10           |\n"
"  |O  O     O   |\n"
"  |      O      |\n"
"  |   O     O   |\n"
"  |             |\n"
"  |   O     O   |\n"
"  |      O      |\n"
"  |   O     O  O|\n"
"  |           10|\n"
"   ------------- \n";

char * cJ = ""
"   ------------- \n"
"  |J            |\n"
"  |O            |\n"
"  |             |\n"
"  |       ╦     |\n"
"  |       ║     |\n"
"  |       ║     |\n"
"  |     ╚═╝     |\n"
"  |             |\n"
"  |            O|\n"
"  |            J|\n"
"   ------------- \n";

char * cQ = ""
"   ------------- \n"
"  |Q            |\n"
"  |O            |\n"
"  |             |\n"
"  |     ╔═╗     |\n"
"  |     ║ ║     |\n"
"  |     ║═╬╗    |\n"
"  |     ╚═╝╚    |\n"
"  |             |\n"
"  |            O|\n"
"  |            Q|\n"
"   ------------- \n";

char * cK = ""
"   ------------- \n"
"  |K            |\n"
"  |O            |\n"
"  |             |\n"
"  |     ╦╔═     |\n"
"  |     ╠╩╗     |\n"
"  |     ║ ║     |\n"
"  |     ╩ ╩     |\n"
"  |             |\n"
"  |            O|\n"
"  |            K|\n"
"   ------------- \n";

char * cJO = ""
"   ------------- \n"
"  |J            |\n"
"  |O            |\n"
"  |K            |\n"
"  |E  /`\\|/`\\   |\n"
"  |R o O o O o  |\n"
"  |    m o m   J|\n"
"  |      W     O|\n"
"  |            K|\n"
"  |            E|\n"
"  |            R|\n"
"   ------------- \n";

void printCard(const char * origin, const char *icon) {
    while(*origin != '\x00'){
        if(*origin == 'O') {
            printf("%s", icon);
        } else {
            printf("%c", *origin);
        }
        origin++;
    }
}

// 카드 출력 시 실제 값과 아이콘이 다른 버그가 있음
void showNewCard(unsigned int hitcard) {
    // puts("[New Card]");
    char * cardshape[NUMBER] = {cA, c2, c3, c4, c5, c6, c7, c8, c9, c10, cJ, cQ, cK};
    // printf("TEST: %s, %d, %d, %d\n", deck[hitcard], hitcard / NUMBER, hitcard % NUMBER, hitcard); // test
    if (hitcard >= JOCKER) { // jocker
        printCard(cJO, "O");
        return;
    }
    printCard(cardshape[hitcard % NUMBER], icon[(hitcard / NUMBER)]);
}
