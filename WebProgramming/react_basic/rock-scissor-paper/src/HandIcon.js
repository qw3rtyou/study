import rockImg from './assets/rock.svg';
import scissorImg from './assets/scissor.svg';
import paperImg from './assets/paper.svg';

const RSP_IMG={
  'rock':rockImg,
  'scissor':scissorImg,
  'paper':paperImg,
}

function HandIcon({value}){
  const srcProp=RSP_IMG[value]
  
  return <img src={srcProp} alt={value}/>;
}

export default HandIcon;