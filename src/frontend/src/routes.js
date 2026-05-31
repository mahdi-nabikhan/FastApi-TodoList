import {Route,Routes,useRoutes} from 'react-router-dom';
import Index from './Pages/IndexPages/Index/Index';
import LoginPage from './Pages/UsersPanel/Login/LoginPage';
import RegisterPage from './Pages/UsersPanel/Register/RegisterPage';
import TODODeatil from './Pages/IndexPages/TODODeatil/TODODeatil';



const routers = [
    {path :"",element:<Index/>},
    {path:'/login',element:<LoginPage/>},
    {path:'/regsiter',element:<RegisterPage/>},
    {path:'/todo/:id',element:<TODODeatil/>}



]
export default routers