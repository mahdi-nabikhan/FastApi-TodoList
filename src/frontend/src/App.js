import logo from './logo.svg';
import './App.css';
import { useRoutes } from 'react-router-dom';
import Navbar from './Components/Navbar/Navbar'
import routers from './routes';
function App() {
  let router = useRoutes(routers)

  return (
    <>
    {router}
    </>
    
  );
}

export default App;
