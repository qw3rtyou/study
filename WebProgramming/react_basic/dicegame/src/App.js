import Board from './Board';
import {useState} from 'react';
import Button from './Button';
import './App.css'

function random(n){
  return Math.ceil(Math.random()*n);
}

function App(){
  const [myHistory,setMyHistory]=useState([]);
  const [otherHistory,setOtherHistory]=useState([]);

  const handleButtonClick = () => {
    const nextNum=random(6);
    setMyHistory([...myHistory,nextNum]);   //배열은 참조형이므로 spread 문법으로 새로 만들어주는게 좋음!
    
    const nextOtherNum=random(6);
    setOtherHistory([...otherHistory,nextOtherNum]); 
  }

  const handleClearClick = () => {
    setMyHistory([]);
    setOtherHistory([]);
  }

  return(
    <div className='App'>
      <div>
        <Button className='App-button' color='blue' onClick={handleButtonClick}>던지기</Button>
        <Button className='App-button' color='red' onClick={handleClearClick}>처음부터</Button>
      </div>
      <div>
        <Board name='나' color='blue' gameHistory={myHistory}/>
        <Board name='상대' color='red' gameHistory={otherHistory}/>
      </div>
    </div>
  )
}

export default App;