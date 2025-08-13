import './MyCard.css'
import cardImage from '../assets/creaditcard.jpeg'

function MyCard () {
    return <div className='contentArea'>
        <h2>My Cards</h2><br></br>

        <div className='mycardsContainer'>
            <div className='cards'>
                <h5>Bus Card</h5>
                <p id='cardnumber'>Card number: 2356 8569 7589 5624</p>
                <img src={cardImage}/>
                <div className='balanceCardContainer'>
                    <div className='balanceCard'>
                        <h6>Balance</h6>
                        <h3>RS.563.00</h3>
                    </div>
                    <div className='balanceCard'>
                        <h6>Status</h6>
                        <h3>Active</h3>
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
                        <h3>RS.265.00</h3>
                    </div>
                    <div className='balanceCard'>
                        <h6>Status</h6>
                        <h3>Active</h3>
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