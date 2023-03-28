import {useState} from 'react';
import Button from './Button';
import Dice from './Dice';

function random(n){
  return Math.ceil(Math.random()*n);
}

function App(){
  const [num,setNum]=useState(1);
  const [sum,setSum]=useState(0);
  const [gameHistory,setGameHistory]=useState([]);

  const handleButtonClick = () => {
    const nextNum=random(6);
    setNum(nextNum);
    setSum(sum+nextNum);
    setGameHistory([...gameHistory,nextNum]);   //배열은 참조형이므로 spread 문법으로 새로 만들어주는게 좋음!
  }

  const handleClearClick = () => {
    setNum(1);
    setSum(0);
    setGameHistory([])
  }

  return (
    <div>
      <div>
        <Button onClick={handleButtonClick}>던지기</Button>
        <Button onClick={handleClearClick}>처음부터</Button>
      </div>
      <div>
        <h2>나</h2>
        <Dice color='blue' num={num}/>
        <h2>총점</h2>
        <p>{sum}</p>
        <h2>기록</h2>
        <p>{gameHistory.join(',')}</p>
      </div>
    </div>
  );
}

export default App;