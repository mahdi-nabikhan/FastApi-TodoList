// routes.js

import MainLayout from './layouts/MainLayout'
import PanelLayout from './layouts/PanelLayout'

import Index from './Pages/IndexPages/Index/Index'
import LoginPage from './Pages/UsersPanel/Login/LoginPage'
import RegisterPage from './Pages/UsersPanel/Register/RegisterPage'
import TODODeatil from './Pages/IndexPages/TODODeatil/TODODeatil'

import Dashboard from './Pages/Panel/Dashboard/Dashboard'
import TodoPage from './Pages/Panel/TodoPage/TodoPage'

const routers = [
  {
    element: <MainLayout />,
    children: [
      {
        path: '/',
        element: <Index />
      },
      {
        path: '/login',
        element: <LoginPage />
      },
      {
        path: '/regsiter',
        element: <RegisterPage />
      },
      {
        path: '/todo/:id',
        element: <TODODeatil />
      }
    ]
  },

  {
    path: '/panel',
    element: <PanelLayout />,
    children: [
      {
        index: true,
        element: <Dashboard />
      },{path:'/todo',index:ture,element:<TodoPage/>}
    ]
  }
]

export default routers