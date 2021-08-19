import React, { useEffect } from "react";
// import { BrowserRouter as Router, Switch, Route } from "react-router-dom"
import Header from "./AppBar"
import { useSelector, useDispatch } from "react-redux"
import { bindActionCreators } from "redux"
import { actionCreators } from "./state/actions/index"
import axios from "axios";

import jwt from 'jwt-decode'

import Content from "./Content"

function App() {

  const state = useSelector((state) => state)

  const dispatch = useDispatch()
  const { AUTH_LOGIN, AUTH_LOGOUT } = bindActionCreators(actionCreators, dispatch)

  useEffect(() => {
    console.log(state)
    const token = localStorage.getItem('access_token')
    if(token != null) {
      const decode = jwt(token)
      axios({
        method: "POST", 
        url: "http://localhost:8000/auth/verify/",
        data: {
          token: token
        },
        withCredentials: true
      })
      .then(response => {
        console.log(response)
      })
      .catch(err => {
        axios({
          method: "GET",
          url: "http://localhost:8000/auth/refresh/",
          withCredentials: true,
        })
        .then(response => {
          const data = response.data
          localStorage.setItem('access_token', data['access'])
        })
        .catch(err => {
          console.log(err)
        })
      })
      AUTH_LOGIN({user:decode['username']})
    } else {
      console.log("HOLA")
      AUTH_LOGOUT({})
    }
  }, [])

  return (
    <>
    <Header></Header>
    <Content></Content>
    </>
  );
}

export default App;