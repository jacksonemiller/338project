import logo from './logo.svg';
import './App.css';
import Chatbox from './components/Chatbox';

function App() {
  return (
    <div className="App">
      <header className="App-header" style={{color: 'black'}}>
        <Chatbox/>
      </header>
    </div>
  );
}

export default App;
