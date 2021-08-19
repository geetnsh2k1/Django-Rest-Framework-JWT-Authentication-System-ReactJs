import axios from 'axios';
import React, { useEffect, useState } from 'react'
import { useSelector } from 'react-redux'
import Message from "./Message"

export default function Content() {

    axios.defaults.headers.common["Authorization"] = `AuthToken ${localStorage.getItem('access_token')}`

    const state = useSelector((state) => state)

    const [data, setData] = useState(null);

    function fetch() {
        if(localStorage.getItem('access_token')) {
            axios({
                method: "GET", 
                url: "http://localhost:8000/auth/google/"
            })
            .then(res => {
                setData(res.data)
            })
            .catch(err => {
                console.log(err)
            })   
        }
    }

    useEffect(() => {
        console.log("Hola")
        fetch()
    }, [state.UserReducer.isAuthenticated]);

    return (
        <div>
            {
                state.UserReducer.register ? <Message message={"You have been successfully registered."}></Message> : ""
            }

            {state.UserReducer.isAuthenticated ? 
               data ? data['Google'] : "Not present" : 
            "Login Please"}
        </div>
    )
}
