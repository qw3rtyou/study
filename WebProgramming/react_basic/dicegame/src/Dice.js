import diceBlue01 from './assets/dice-blue-1.svg';
import diceBlue02 from './assets/dice-blue-2.svg';
import diceBlue03 from './assets/dice-blue-3.svg';
import diceBlue04 from './assets/dice-blue-4.svg';
import diceBlue05 from './assets/dice-blue-5.svg';
import diceBlue06 from './assets/dice-blue-6.svg';
import diceRed01 from './assets/dice-red-1.svg';
import diceRed02 from './assets/dice-red-2.svg';
import diceRed03 from './assets/dice-red-3.svg';
import diceRed04 from './assets/dice-red-4.svg';
import diceRed05 from './assets/dice-red-5.svg';
import diceRed06 from './assets/dice-red-6.svg';

const DICE_IMAGES={
    blue: [diceBlue01,diceBlue02,diceBlue03,diceBlue04,diceBlue05,diceBlue06],
    red: [diceRed01,diceRed02,diceRed03,diceRed04,diceRed05,diceRed06],
};


function Dice(props) {
    const src=DICE_IMAGES[props.color][props.num-1];
    const alt=`${props.color} ${props.num}`;

    return <img src={src} alt={alt}/>;
}

export default Dice;