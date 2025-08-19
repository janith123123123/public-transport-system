import {useForm} from 'react-hook-form';
import { useState } from 'react';
import {yupResolver} from '@hookform/resolvers/yup';
import * as Yup from 'yup';
import '../pages/Log-in.css'
import { useNavigate } from 'react-router-dom';

const schema = Yup.object().shape({
    username: Yup.string().required('Username is required'),
    password: Yup.string().min(8).required('Password is required'),
});

function Login() {
    const navigate = useNavigate();
    const [loginError, setLoginError] = useState('')

    const { register, handleSubmit,formState: {errors}} = useForm({
        resolver: yupResolver(schema),
        
    });
    console.log(" Validation errors:", errors);
    const onSubmit = async(data) => {console.log('loged in:', data);
        setLoginError('');
        try {
            const res = await fetch('http://127.0.0.1:8000/api/token/',{
                method:'POST',
                headers:{'Content-Type':'application/json'},
                body:JSON.stringify({
                    username:data.username,
                    password:data.password,
                }),
            });

            const result = await res.json();

            if (res.ok) {
                console.log('Access Token:', result.access);

                localStorage.setItem('access',result.access);

                localStorage.setItem('refresh',result.refresh);

                navigate('/dashboard');
            }else{
                setLoginError(result.detail ||'Inalid username or password.')
            }
        }catch(err){
            setLoginError('Unable to connect to server.Please try again.')
            console.error('login failed:',err);
        }
    };

    return (
        <div className='loginContainer'>
            <div>
                <h1>Log In</h1>
            </div>
        
            <form onSubmit={handleSubmit(onSubmit)}>
                <input {...register('username')} placeholder='username' />
                <p>{errors.username?.message}</p>

                <input {...register('password')} type='password' placeholder='Password' />
                <p>{errors.password?.message}</p>

                {loginError && <p className="error">{loginError}</p>}

                <button type='submit'>Log In</button>
            </form>
        </div>

    );
}

export default Login;