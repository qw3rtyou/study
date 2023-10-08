// LED_OnOff 함수
void LED_OnOff(int led, int interval) 
{
    HAL_GPIO_WritePin(GPIO_LED, led, GPIO_PIN_SET );
    HAL_Delay(interval);
    HAL_GPIO_WritePin(GPIO_LED, led, GPIO_PIN_RESET );
}

// while문 안에 들어갈거
unsigned char led = 0x01;

if(HAL_GPIO_ReadPin(GPIO_SW, SW1)==RESET) {
    do{
        LED_OnOff(led, 200);
        led=led<<1;
        led=led&0xfe;
        if(led==0x80) led = 0x01;
    } while(true)
}
if(HAL_GPIO_ReadPin(GPIO_SW, SW2)==RESET) {
    do{
        LED_OnOff(led, 200);
        led=led<<1;
        led=led&0xfe;
        if(led==0x20) led = 0x01;
    } while(true)
}
if(HAL_GPIO_ReadPin(GPIO_SW, SW3)==RESET) {
    do{
        LED_OnOff(led, 200);
        led=led<<1;
        led=led&0xfe;
        if(led==0x08) led = 0x01;
    } while(true)
}
if(HAL_GPIO_ReadPin(GPIO_SW, SW4)==RESET) {
    do{
        LED_OnOff(led, 200);
        led=led<<1;
        led=led&0xfe;
        if(led==0x02) led = 0x01;
    } while(true)
}

LED_OnOff (led, 100);


