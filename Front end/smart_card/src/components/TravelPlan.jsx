import './TravelPlan.css'

function TravelPlan () {

    return <div className='TravelPlanContentArea'>
        <div>
            <h1>Plan Your Journey</h1>
            
            <div className='planBuilderCard'>
                <form>
                    <label htmlFor="card">Card</label><br/>
                    <select id="card" name="card">
                        <option value="">Select a Card</option>
                        <option value="busCard">Bus Card</option>
                        <option value="trainCard">Train Card</option>
                    </select>
                    <br />
                    <label htmlFor="plan">Plan</label><br/>
                    <select id="plan" name="plan">
                        <option value="">Select a plan</option>
                        <option value="monthly">Monthly</option>
                        <option value="weekly">Weekly</option>
                        <option value="student">Student</option>
                    </select>
                </form>
            </div>
        </div>

        <div>
            <h1>My Plans</h1>
        </div>
        
    </div>

}

export default TravelPlan;