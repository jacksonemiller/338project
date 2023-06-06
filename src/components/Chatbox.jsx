import React, { useState } from 'react';
import ChatMsg from '@mui-treasury/components/chatMsg/ChatMsg';

const Chatbox = () => {
  
  const [inputText, setInputText] = useState('');
  const [messages, setMessages] = useState([]);

  const appendMessage = (msg) => {
    setMessages([...messages, msg])
  }

  const queryBot = (prompt, cache) => {
    fetch("http://127.0.0.1:8000/chatbot/",
          {method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          }, body: JSON.stringify([...messages, prompt])}
    ).then(response => {
      return response.text();
    }).then(text => {
      setMessages([...cache, prompt, text])
    });
  }

  const updateEverything = () => {
    const prompt = inputText
    const msgCache = messages
    appendMessage(inputText)
    setInputText('')
    queryBot(prompt, msgCache)
  }

  return (<div style={{borderStyle: 'solid',
                       overflow: 'auto',
                       height: '500px',
                       width: '1000px'}}>
    <div style={{height: '95%', whiteSpace: 'pre-line'}}>
    {
      messages.map((message, index) => (
      <ChatMsg
        side={!(index % 2) ? 'right' : 'left'}
        avatar={''}
        messages={[message]}
      />))
    }
    </div>
    <input
      style={{position: 'absolute',
              bottom: '0',
              left: '30%',
              width: '40%'}}
      type="text"
      value={inputText}
      onChange={(e) => {setInputText(e.target.value)}}
      onKeyDown={(e) => {
        if (e.key === 'Enter') {
          updateEverything();
        }
      }}/>
  </div>
)};

export default Chatbox;