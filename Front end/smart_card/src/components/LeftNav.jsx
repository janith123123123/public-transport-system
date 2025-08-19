import './LeftNav.css'
import { Link } from 'react-router-dom';
import { useState } from 'react';
import busIcon from '../assets/bus-front.svg'
import cardIcon from '../assets/credit-card-2-back-fill.svg'
import rechargeIcon from '../assets/wallet2.svg'
import historyIcon from '../assets/clock-history.svg'
import MyCard from './MyCard';
import TopUp from './TopUp';
import TravelPlan from './TravelPlan';



function LeftNav ({setActiveComponent,activeComponent}) {

    return <><div className="leftnav">
        <ul>
            <li onClick={()=> setActiveComponent('cards')} className={activeComponent === 'cards' ? 'active':''}><img src={cardIcon}/>Cards</li>
            <li onClick={()=> setActiveComponent('topup')} className={activeComponent === 'topup' ? 'active':''}><img src={rechargeIcon}/>Top-Up</li>
            <li onClick={()=> setActiveComponent('travelPlan')} className={activeComponent === 'travelPlan' ? 'active':''}><img src={busIcon}/>Travel Plan</li>
            <li onClick={()=> setActiveComponent('travelHistory')} className={activeComponent === 'travelHistory' ? 'active':''}><img src={historyIcon}/>Travel History</li>
        </ul>
    </div>
    
    </>
}

export default LeftNav;