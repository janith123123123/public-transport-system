import { Routes,Route } from "react-router-dom";
import { useState } from "react";
import MyCard from "./MyCard";
import TopUp from "./TopUp";
import TravelPlan from "./TravelPlan";
import LeftNav from "./LeftNav";
import TravelHistory from "./TravelHistory";

function Dashboard () {

    const [activeComponent,setActiveComponent] = useState('cards');

    const renderComponent = () => {
        switch (activeComponent) {
            case 'cards':
                return <MyCard />
            case 'topup':
                return <TopUp />
            case 'travelPlan':
                return <TravelPlan />
            case 'travelHistory':
                return <TravelHistory />
            default:
                return null;
        }
    };

    return <div>
        <LeftNav setActiveComponent={setActiveComponent} activeComponent={activeComponent}/>
        {renderComponent()}
    </div>
}

export default Dashboard;