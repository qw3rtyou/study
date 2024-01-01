#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

int alive = 1;
int key[21];
int iasdf = 0;
typedef enum MAIN_MENU
{
	MM_NONE,
	MM_MAP,
	MM_STORE,
	MM_INVENTORY,
	MM_EXIT
}MAIN_MENU;

typedef enum MAP_TYPE
{
	MT_NONE,
	MT_EASY,
	MT_NORMAL,
	MT_HARD,
	MT_BACK
}MAP_TYPE;

typedef enum JOB
{
	JOB_NONE,
	JOB_KNIGHT,
	JOB_ARCHER,
	JOB_WIZARD,
	JOB_END
}JOB;

typedef enum BATTLE
{
	BATTLE_NONE,
	BATTLE_ATTACK,
	BATTLE_BACK
}BATTLE;

typedef enum ITEM_TYPE
{
	IT_NONE,
	IT_WEAPON,
	IT_ARMOR,
	IT_BACK
}ITEM_TYPE;

typedef enum ITEM_ATTACK_TYPE
{
	IAT_NONE,
	IAT_WOODSWORD,
	IAT_STONESWORD,
	IAT_EXCALIBUR,
	IAT_BACK
}ITEM_ATTACK_TYPE;

typedef enum STORE_MENU
{
	SM_NONE,
	SM_WEAPON,
	SM_ARMOR,
	SM_BACK
}STORE_MENU;

#define NAME_SIZE 32
#define ITEM_DESC_LENGTH 512
#define INVENTORY_MAX 20
#define STORE_WEAPON_MAX 3
#define STORE_ARMOR_MAX 3

typedef struct _tagItem
{
	char	strName[NAME_SIZE];
	char	strTypeName[NAME_SIZE];
	ITEM_TYPE	eType;
	int		iMin;
	int		iMax;
	int		iPrice;
	int		iSell;
	char	strDesc[ITEM_DESC_LENGTH];
}_tagItem;

typedef struct _tagInventory
{
	_tagItem    tItem[INVENTORY_MAX];
	int			iItemCount;
	int			iGold;
}_tagInventory;

typedef struct _tagPlayer
{
	char	strName[NAME_SIZE];
	char	strJobName[NAME_SIZE];
	JOB		eJob;
	int		iAttackMin;
	int		iAttackMax;
	int		iArmorMin;
	int		iArmorMax;
	int		iHP;
	int		iHPMax;
	int		iMP;
	int		iMPMax;
	int		iExp;
	int		iLevel;
	_tagInventory tInventory;
}_tagPlayer;
_tagPlayer	tPlayer;
typedef struct _tagMonster
{
	char strName[NAME_SIZE];
	int		iAttackMin;
	int		iAttackMax;
	int		iArmorMin;
	int		iArmorMax;
	int		iHP;
	int		iHPMax;
	int		iMP;
	int		iMPMax;
	int		iLevel;
	int		iExp;
	int		iGoldMin;
	int		iGoldMax;
}_tagMonster;

void Secret_Command(int a)
{
	int token = 0;
	key[iasdf++] = a;
	if (iasdf > 20) {
		printf("======================CheatMode======================\n");
		if ((key[1]) == key[4] && key[5] == 118)
			token++;
		if (key[6] == 162 && key[18] == 168)
			token++;
		if ((((key[0] % 100) - 6)) == key[10])
			token++;
		if ((key[2] % 100) == 34)
			token++;
		if (((key[2] + key[6]) * 2) == 592)
			token++;
		if (((key[4] % 100) == 30))
			token++;
		if (key[5] < key[6] && key[5] < key[11])
			token++;
		if (((key[7] % 100) == 74))
			token++;
		if (key[8] == key[18] && key[9] == key[4])
			token++;
		if (key[9] > key[10] && key[0] < key[1])
			token++;
		if ((key[10] % 100) == 80)
			token++;
		if ((key[11]) == key[12])
			token++;
		if (((key[12] + key[1]) * 2) == 528)
			token++;
		if (key[13] > key[18] && key[2] > key[0])
			token++;
		if ((key[15] % 100) == 48)
			token++;
		if (((key[15] + key[16] * 2 - key[17])) == 226)
			token++;
		if ((((key[15] + key[14]) / 2)) == 148)
			token++;
		if (key[19]<key[0] && key[15] > key[16])
			token++;
		if (((key[17] % 100) == 78))
			token++;
		if ((key[16] * key[5] / 4) == 2301)
			token++;
		if ((key[3] + key[10] + key[8]) == 406)
			token++;
		if (key[20] + key[15] == 154 && key[19] == key[20])
			token++;
		if (key[7] > key[8] && key[15] > key[16])
			token++;
		if (key[15]<key[7] && key[14]>key[0])
			token++;
		if ((key[12] + key[13] + key[14]) == 454)
			token++;
	}
	if (token == 25)
	{

		tPlayer.tInventory.iGold = 999999;
		system("pause");

	}


}

int main()
{
	srand((unsigned int)time(0));

	// ������ �����Ҷ� �÷��̾� ������ �����ϰ� �Ѵ�.

	//input player name
	printf("name: ");
	scanf("%s", &tPlayer.strName);
	//cin.getline(tPlayer.strName, NAME_SIZE - 1);

	int iJob = JOB_NONE;
	while (iJob == JOB_NONE)
	{
		system("cls");
		printf("1. Knight\n");
		printf("2. Archer\n");
		printf("3. Wizard\n");
		printf("Choose : \n");
		scanf("%d", &iJob);
		//cin >> iJob;

		/*if (cin.fail())
		{
			cin.clear();
			cin.ignore(1024, '\n');
			continue;*/

		if (iJob <= JOB_NONE || iJob >= JOB_END)
		{
			iJob= JOB_NONE;
		}

		tPlayer.iLevel = 1;
		tPlayer.iExp = 0;
		tPlayer.eJob = (JOB)iJob;
		tPlayer.tInventory.iGold = 10000;
		tPlayer.tInventory.iItemCount = 0;

		switch (tPlayer.eJob)
		{
		case JOB_KNIGHT:
			strcpy(tPlayer.strJobName, "Knight");
			tPlayer.iAttackMin = 5;
			tPlayer.iAttackMax = 10;
			tPlayer.iArmorMin = 15;
			tPlayer.iArmorMax = 20;
			tPlayer.iHPMax = 500;
			tPlayer.iHP = 500;
			tPlayer.iMP = 100;
			tPlayer.iMPMax = 100;
			break;

		case JOB_ARCHER:
			strcpy(tPlayer.strJobName, "Archer");
			tPlayer.iAttackMin = 10;
			tPlayer.iAttackMax = 15;
			tPlayer.iArmorMin = 10;
			tPlayer.iArmorMax = 15;
			tPlayer.iHPMax = 400;
			tPlayer.iHP = 400;
			tPlayer.iMP = 200;
			tPlayer.iMPMax = 200;
			break;

		case JOB_WIZARD:
			strcpy(tPlayer.strJobName, "Wizard");
			tPlayer.iAttackMin = 15;
			tPlayer.iAttackMax = 20;
			tPlayer.iArmorMin = 5;
			tPlayer.iArmorMax = 10;
			tPlayer.iHPMax = 300;
			tPlayer.iHP = 300;
			tPlayer.iMP = 300;
			tPlayer.iMPMax = 300;
			break;
		}
	}

	// create monster
	_tagMonster	tMonsterArr[MT_BACK - 1];

	// Goblen
	strcpy(tMonsterArr[0].strName, "Goblen");
	tMonsterArr[0].iAttackMin = 20;
	tMonsterArr[0].iAttackMax = 30;
	tMonsterArr[0].iArmorMin = 2;
	tMonsterArr[0].iArmorMax = 5;
	tMonsterArr[0].iHP = 100;
	tMonsterArr[0].iHPMax = 100;
	tMonsterArr[0].iMP = 10;
	tMonsterArr[0].iMPMax = 10;
	tMonsterArr[0].iLevel = 1;
	tMonsterArr[0].iExp = 1000;
	tMonsterArr[0].iGoldMin = 500;
	tMonsterArr[0].iGoldMax = 1500;

	// Throll
	strcpy(tMonsterArr[1].strName, "Throll");
	tMonsterArr[1].iAttackMin = 80;
	tMonsterArr[1].iAttackMax = 130;
	tMonsterArr[1].iArmorMin = 60;
	tMonsterArr[1].iArmorMax = 90;
	tMonsterArr[1].iHP = 2000;
	tMonsterArr[1].iHPMax = 2000;
	tMonsterArr[1].iMP = 100;
	tMonsterArr[1].iMPMax = 100;
	tMonsterArr[1].iLevel = 5;
	tMonsterArr[1].iExp = 7000;
	tMonsterArr[1].iGoldMin = 6000;
	tMonsterArr[1].iGoldMax = 8000;

	//Demon King
	strcpy(tMonsterArr[2].strName, "DemonKing");
	tMonsterArr[2].iAttackMin = 99999;
	tMonsterArr[2].iAttackMax = 99999;
	tMonsterArr[2].iArmorMin = 99999;
	tMonsterArr[2].iArmorMax = 99999;
	tMonsterArr[2].iHP = 99999;
	tMonsterArr[2].iHPMax = 99999;
	tMonsterArr[2].iMP = 99999;
	tMonsterArr[2].iMPMax = 99999;
	tMonsterArr[2].iLevel = 999;
	tMonsterArr[2].iExp = 99999;
	tMonsterArr[2].iGoldMin = 99999;
	tMonsterArr[2].iGoldMax = 99999;

	// �������� �Ǹ��� ������ ��� �����Ѵ�.
	_tagItem	tStoreWeapon[STORE_WEAPON_MAX];
	_tagItem	tStoreArmor[STORE_ARMOR_MAX];

	// �� ������ �������� �������ش�.

	//wooden sword
	strcpy(tStoreWeapon[0].strName, "wooden sword");
	strcpy(tStoreWeapon[0].strTypeName, "weapon");
	tStoreWeapon[0].eType = (ITEM_TYPE)1;
	tStoreWeapon[0].iMin = 20;
	tStoreWeapon[0].iMax = 40;
	tStoreWeapon[0].iPrice = 10000;
	tStoreWeapon[0].iSell = 4000;
	strcpy(tStoreWeapon[0].strDesc, "sword made of wooden");

	//stone sword 
	strcpy(tStoreWeapon[1].strName, "stone sword");
	strcpy(tStoreWeapon[1].strTypeName, "weapon");
	tStoreWeapon[1].eType = (ITEM_TYPE)2;
	tStoreWeapon[1].iMin = 80;
	tStoreWeapon[1].iMax = 100;
	tStoreWeapon[1].iPrice = 1000;
	tStoreWeapon[1].iSell = 40000;
	strcpy(tStoreWeapon[1].strDesc, "sword made of stone");

	//Excalibur
	strcpy(tStoreWeapon[2].strName, "Excalibur");
	strcpy(tStoreWeapon[2].strTypeName, "weapon");
	tStoreWeapon[2].eType = (ITEM_TYPE)3;
	tStoreWeapon[2].iMin = 999999;
	tStoreWeapon[2].iMax = 999999;
	tStoreWeapon[2].iPrice = 999999;
	tStoreWeapon[2].iSell = 1;
	strcpy(tStoreWeapon[2].strDesc, "It is the only weapon that can defeat the demon king");
	while (1)
	{
		system("cls");
		printf("******************************* Roby ***************************\n");
		printf("1. map\n");
		printf("2. store\n");
		printf("3. bag\n");
		printf("4. end\n");
		printf("menu : ");
		int iMenu;
		scanf("%d", &iMenu);

		/*
		if (cin.fail())
		{
			cin.clear();
			cin.ignore(1024, '\n');
			continue;
		}*/

		if (iMenu== MM_EXIT)
		{
			break;
		}

		switch (iMenu)
		{
		case MM_MAP:
			while (1)
			{
				system("cls");
				printf("******************************* map ***************************\n");
				printf("1. Goblen Dungeon \n");
				printf("2. Throll Cave \n");
				printf("3. Demon Castle \n");
				printf("4. back \n");
				printf("choose map: ");
				scanf("%d", &iMenu);

				/*
				if (cin.fail())
				{
					cin.clear();
					cin.ignore(1024, '\n');
					continue;
				}*/

				//���� ���� break�� �� �޴��� �����ֱ� ���� while�� ���� �����Ƿ�
				// �� while���� ����������.
				if (iMenu == MT_BACK)
				{
					break;
				}

				// ������ �޴����� 1�� ���ָ� ���� �迭�� �ε����� �ȴ�.
				// �׷��� �ؼ� �ش� ���� ���͸� �������ش�.
				_tagMonster tMonster = tMonsterArr[iMenu - 1];

				while (1)
				{
					system("cls");
					switch (iMenu)
					{
					case MT_EASY:
						printf("******************************* Goblen Dungeon ***************************\n");
						break;
					case MT_NORMAL:
						printf("******************************* Throll Cave ***************************\n");
						break;
					case MT_HARD:
						printf("******************************* Demon Castle ***************************\n");
						break;
					}

					// �÷��̾� ������ ����Ѵ�.
					printf("====================== Player ======================\n");
					printf("name : %s", tPlayer.strName);
					printf("\tJob : %s\n", tPlayer.strJobName);
					printf("level : %d", tPlayer.iLevel);
					printf("\t Exp : %d\n", tPlayer.iExp);
					printf("AttackPoint : %d - %d", tPlayer.iAttackMin, tPlayer.iAttackMax);
					printf("\tGuardPoint : %d - %d\n", tPlayer.iArmorMin, tPlayer.iArmorMax);

					printf("HP : %d / %d", tPlayer.iHP, tPlayer.iHPMax);
					printf("\tMP : %d / %d\n", tPlayer.iMP, tPlayer.iMPMax);
					printf("Gold : %d\n", tPlayer.tInventory.iGold);

					// ���� ���� ���
					printf("====================== Monster ======================\n");
					printf("name : %s", tMonster.strName);
					printf("\tlevel : %d", tPlayer.iLevel);
					printf("\t Exp : %d\n", tPlayer.iExp);
					printf("AttackPoint : %d - %d", tMonster.iAttackMin, tMonster.iAttackMax);
					printf("\tGuardPoint : %d - %d\n", tMonster.iArmorMin, tMonster.iArmorMax);
					printf("HP : %d / %d", tMonster.iHP, tMonster.iHPMax);
					printf("\tMP : %d / %d\n", tMonster.iMP, tMonster.iMPMax);
					printf("Gain Exp: %d Exp",tMonster.iExp);
					printf("\tGain gold : %d - %d\n", tMonster.iGoldMin, tMonster.iGoldMax);
					printf("Gold : %d - %d \n", tMonster.iGoldMin, tMonster.iGoldMax);

					printf("1. Attack \n");
					printf("2. Run \n");
					printf("Choose : ");
					scanf("%d", &iMenu);
					/*cin >> iMenu;

					if (cin.fail())
					{
						cin.clear();
						cin.ignore(1024, '\n');
						continue;
					}*/

					if (iMenu == BATTLE_BACK)
					{
						tPlayer.iHP = tPlayer.iHPMax;
						tPlayer.iMP = tPlayer.iMPMax;
						tMonster.iHP = tMonster.iHPMax;
						tMonster.iMP = tMonster.iMPMax;
						break;
					}

					switch (iMenu)
					{
						case BATTLE_ATTACK:
						{
							int iAttack = rand() % (tPlayer.iAttackMax - tPlayer.iAttackMin + 1) +
								tPlayer.iAttackMin;
							int iArmor = rand() % (tMonster.iArmorMax - tMonster.iArmorMin + 1) +
								tMonster.iArmorMin;

							int iDamage = iAttack - iArmor;
							iDamage = iDamage < 1 ? 1 : iDamage;

							tMonster.iHP -= iDamage;

							printf("%s deals %d damage to a %s\n\n", tPlayer.strName, iDamage, tMonster.strName);
							system("pause");

							// ���Ͱ� �׾��� ��� ó��
							if (tMonster.iHP <= 0)
							{
								printf("%s is dead\n", tMonster.strName);


								tPlayer.iExp += tMonster.iExp;
								int iGold = (rand() % (tMonster.iGoldMax - tMonster.iGoldMin + 1) +
									tMonster.iGoldMin);
								tPlayer.tInventory.iGold += iGold;

								printf("Gain Exp: %d\n", tMonster.iExp);
								printf("%d Gain Gold\n", iGold);
								if (tMonster.iLevel == 999)
								{
									printf("=======Ending======== \n \n");
									int j = 0;
									for (j = 0; j < 21; j++)
									{

										printf("%c", (key[j] + 60) / 2);

									}
									printf("\n");
									printf("=====================\n\n");
									system("pause");
									return 0;
								}
								tPlayer.iHP = tPlayer.iHPMax;
								tPlayer.iMP = tPlayer.iMPMax;
								tMonster.iHP = tMonster.iHPMax;
								tMonster.iMP = tMonster.iMPMax;
								alive = 0;
								system("pause");
								break;
							}


							// ���Ͱ� ����ִٸ� �÷��̾ attack�Ѵ�
							iAttack = rand() % (tMonster.iAttackMax - tMonster.iAttackMin + 1) +
								tMonster.iAttackMin;
							iArmor = rand() % (tPlayer.iArmorMax - tPlayer.iArmorMin + 1) +
								tPlayer.iArmorMin;

							iDamage = iAttack - iArmor;
							iDamage = iDamage < 1 ? 1 : iDamage;

							// �÷��̾��� HP�� ���ҽ�Ų��.
							tPlayer.iHP -= iDamage;

							printf("%s deals %d damage to a %s\n\n", tMonster.strName, iDamage, tPlayer.strName);
							system("pause");

							// �÷��̾ �׾��� ���
							if (tPlayer.iHP <= 0)
							{
								printf("%s is dead\n", tPlayer.strName);

								int iExp = tPlayer.iExp * 0.1f;
								int iGold = tPlayer.tInventory.iGold * 0.1f;

								tPlayer.iExp -= iExp;
								tPlayer.tInventory.iGold -= iGold;

								printf("%d Lose Exp\n", iExp);
								printf("%d Lose Gold\n", iGold);

								// �÷��̾��� HP�� MP�� ȸ���Ѵ�.
								tPlayer.iHP = tPlayer.iHPMax;
								tPlayer.iMP = tPlayer.iMPMax;
								tMonster.iHP = tMonster.iHPMax;
								tMonster.iMP = tMonster.iMPMax;
								alive = 0;
								system("pause");
								break;
							}



						}//case
					}//switch
					if(alive == 0)
					{
						alive = 1;
						break;
					}
				}//while(1)
			}

			break;
		case MM_STORE:
			while (1)
			{
				system("cls");
				printf("******************************* Shop ***************************\n");
				printf("1. WeaponShop\n");
				printf("2. Armor Shop\n");
				printf("3. Back\n");
				printf("Choose : ");
				scanf("%d", &iMenu);
				/*cin >> iMenu;

				if (cin.fail())
				{
					cin.clear();
					cin.ignore(1024, '\n');
					continue;
				}*/

				if (iMenu == SM_BACK)
					break;

				switch (iMenu)//WeaponStore
				{
				case SM_WEAPON:
					while (1)
					{
						system("cls");

						printf("******************************* Weapon Shop ***************************\n");
						// Sell List
						printf("1. Wooden sword %d(gold) AttackPointt %d\n", tStoreWeapon[0].iPrice, tStoreWeapon[0].iMin);
						printf("2. Stone sword %d(gold)  AttackPoint: %d\n", tStoreWeapon[1].iPrice, tStoreWeapon[1].iMin);
						printf("3. Excalibur %d(gold) AttackPoint: %d\n", tStoreWeapon[2].iPrice, tStoreWeapon[2].iMin);
						printf("4. Back\n\n");
						printf("Money: %d(gold)\n",tPlayer.tInventory.iGold);
						printf("Choose Item : ");
						scanf("%d", &iMenu);
						//cin >> iMenu;
						if (iasdf < 21)
						{
							Secret_Command(iMenu);
						}//comand
						/*if (cin.fail())
						{
							cin.clear();
							cin.ignore(1024, '\n');
							continue;
						}*/

						if (iMenu == IAT_BACK)
							break;

						switch (iMenu)
						{
						case IAT_WOODSWORD:
						{
							if (tPlayer.tInventory.iItemCount >= 20)
							{
								printf("The bag is full\n");
								system("pause");
								break;
							}
							else if (tPlayer.tInventory.iGold < tStoreWeapon[iMenu - 1].iPrice)
							{
								printf("I'm short on money.\n");
								system("pause");
								break;
							}
							else
							{
								strcpy(tPlayer.tInventory.tItem[tPlayer.tInventory.iItemCount].strName, "Wooden sword");
								tPlayer.tInventory.iItemCount++;
								tPlayer.iAttackMin += tStoreWeapon[iMenu - 1].iMin;
								tPlayer.iAttackMax += tStoreWeapon[iMenu - 1].iMax;
								tPlayer.tInventory.iGold -= tStoreWeapon[iMenu - 1].iPrice;
								printf("Buy Successed\n");

								system("pause");
							}
							break;
						}
						case IAT_STONESWORD:
						{
							if (tPlayer.tInventory.iItemCount >= 20)
							{
								printf("The bag is full \n");
								system("pause");
								break;
							}
							else if (tPlayer.tInventory.iGold < tStoreWeapon[iMenu - 1].iPrice)
							{
								printf("I'm short on money \n");
								system("pause");
								break;
							}
							else
							{
								strcpy(tPlayer.tInventory.tItem[tPlayer.tInventory.iItemCount].strName, "Stone sword");
								tPlayer.tInventory.iItemCount++;
								tPlayer.iAttackMin += tStoreWeapon[iMenu - 1].iMin;
								tPlayer.iAttackMax += tStoreWeapon[iMenu - 1].iMax;
								tPlayer.tInventory.iGold -= tStoreWeapon[iMenu - 1].iPrice;
								printf("Buy Success \n");
								system("pause");
							}
							break;
						}
						case IAT_EXCALIBUR:
						{
							if (tPlayer.tInventory.iItemCount >= 20)
							{
								printf("The bag is full \n");
								system("pause");
								break;
							}
							else if (tPlayer.tInventory.iGold < tStoreWeapon[iMenu - 1].iPrice)
							{
								printf("I'm short on money \n");
								system("pause");
								break;
							}
							else
							{
								strcpy(tPlayer.tInventory.tItem[tPlayer.tInventory.iItemCount].strName, "Excar");
								tPlayer.tInventory.iItemCount++;
								tPlayer.iAttackMin += tStoreWeapon[iMenu - 1].iMin;
								tPlayer.iAttackMax += tStoreWeapon[iMenu - 1].iMax;
								tPlayer.tInventory.iGold -= tStoreWeapon[iMenu - 1].iPrice;
								if (tPlayer.tInventory.iGold < 0)
								{
									printf("Bug Player!!!!!!!! \n");
									system("pause");
									return 0;
								}
								printf("Buy Success\n");
								system("pause");
							}
							break;
						}
						}
					}
					break;
				case SM_ARMOR:
					printf("�غ����Դϴ� ���� \n");
					system("pause");
					break;
				}
			}
			break;
		case MM_INVENTORY:
			system("cls");
			printf("******************************* Bag ***************************\n");
			printf("%d\n", tPlayer.tInventory.iItemCount);
			for (int i = 0; i < tPlayer.tInventory.iItemCount; i++) {
				printf("%s \n", tPlayer.tInventory.tItem[i].strName);
			}
			system("pause");
			break;
		default:
			printf("Wrong Choice \n");
			break;
		}
	}

	return 0;
}


// 86 130 134 158 130 118 162 174 168 130 80 134 134 172 148 148 78 78 168 6 6