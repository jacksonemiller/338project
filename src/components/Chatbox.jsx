import React, { useState, useEffect } from 'react';
import ChatMessages from './ChatMessages';

function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

const Chatbox = () => {
  
  const [inputText, setInputText] = useState('');
  const [currMessage, setCurrMessage] = useState(0);

  useEffect(() => {
    async function delayedUpdate() {
      await delay(2000);
      setCurrMessage(currMessage => currMessage + 1);
    }

    if (currMessage == 1 || currMessage == 3) {
      delayedUpdate();
    }
  }, [currMessage]);

  return (<div style={{borderStyle: 'solid',
                       overflow: 'auto',
                       height: '500px',
                       width: '1000px'}}>
    <ChatMessages currMessage={currMessage}/>
    <input
      style={{position: 'absolute',
              bottom: '0',
              left: '30%',
              width: '40%'}}
      type="text"
      value={inputText}
      onChange={(e) => { setInputText(e.target.value)}}
      onKeyDown={(e) => {
        if (e.key === 'Enter') {
          setInputText('');
          setCurrMessage(currMessage + 1)
        }
      }}/>
  </div>
)};

export default Chatbox;