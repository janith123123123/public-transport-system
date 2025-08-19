import React from 'react'
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'
import './App.css'
import Header from './components/Header'
import LeftNav from './components/LeftNav'
import MyCard from './components/MyCard'
import Dashboard from './components/Dashboard'
import Login from './pages/Log-in'

function ProtectedRoute ({children}) {
  const token = localStorage.getItem('access');
  return token ? children : <Navigate to ='/login' replace />
}

function App() {


  return (
    <Router>
      <Routes>
        <Route path='/login' element={<Login />}/>
        <Route path='/dashboard' element={
          <ProtectedRoute>
            <Header /> 
            <LeftNav /> 
            <Dashboard />
          </ProtectedRoute>
        }/>
        <Route path="dashboard" element={<Dashboard />}/>
        <Route path="*" element={<Navigate to="/login" replace />} />
      </Routes>
    </Router>
    
  );
}

export default App
