import { useState,useEffect } from 'react';
import './MyCard.css'
import cardImage from '../assets/creaditcard.jpeg'

function MyCard () {

    const [busBalance,setBusBalance] = useState('--');
    const [trainBalance,setTrainBalance] = useState('--');
    const [busCardStatus,setBusCardStatus] = useState('--');
    const [trainCardStatus,setTrainCardStatus] = useState('--');

    useEffect(() => {
        async function fetchData() {
            const token = localStorage.getItem('access');

            const res = await fetch('http://127.0.0.1:8000/api/cards/', {
                method: 'GET',
                headers: {
                    'Content-Type':'application/json',
                    'Authorization': `Bearer ${token}`,
                },
            });

            if (res.ok) {
                const result = await res.json();
                console.log(result);

                result.forEach(card => {
                    const category = card.card_category;
                    const status = card.card_state;

                    if (category === 1){
                        setBusBalance(card.balance);
                        setBusCardStatus(status === 1 ? 'Active' : 'Disabled');
                    }else if (category === 2) {
                        setTrainBalance(card.balance);
                        setTrainCardStatus(status === 1 ? 'Active' : 'Disabled');
                    }    
                });
                
            }
        }

        fetchData();
    }, []);

    

    return <div className='MyCardContentArea'>
        <div className='title'>
            <h2>My Cards</h2><br></br>
            <form>
                <button>Add Card</button>
            </form>
        </div>

        <div className='mycardsContainer'>
            <div className='cards'>
                <h5>Bus Card</h5>
                <p id='cardnumber'>Card number: 2356 8569 7589 5624</p>
                <img src={cardImage}/>
                <div className='balanceCardContainer'>
                    <div className='balanceCard'>
                        <h6>Balance</h6>
                        <h3>RS.{busBalance}</h3>
                    </div>
                    <div className='balanceCard'>
                        <h6>Status</h6>
                        <h3>{busCardStatus}</h3>
                    </div>
                </div>
                <form>
                    <button>Top-Up</button>
                </form>
            </div>

            <div className='cards'>
                <h5>Train Card</h5>
                <p id='cardnumber'>Card number: 8456 8524 7842 9546</p>
                <img src={cardImage}/>
                <div className='balanceCardContainer'>
                    <div className='balanceCard'>
                        <h6>Balance</h6>
                        <h3>RS.{trainBalance}</h3>
                    </div>
                    <div className='balanceCard'>
                        <h6>Status</h6>
                        <h3>{trainCardStatus}</h3>
                    </div>
                </div>
                <form>
                    <button>Top-Up</button>
                </form>
            </div>
        </div>

    </div>
}

export default MyCard;