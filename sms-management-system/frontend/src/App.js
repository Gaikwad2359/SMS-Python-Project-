import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import ProgramControl from './components/ProgramControl';
import CountryOperator from './components/CountryOperator';
import Login from './components/Login';

const App = () => {
    return (
        <Router>
            <div>
                <h1>SMS Management System</h1>
                <Switch>
                    <Route path="/" exact component={Login} />
                    <Route path="/dashboard" component={Dashboard} />
                    <Route path="/program-control" component={ProgramControl} />
                    <Route path="/country-operator" component={CountryOperator} />
                </Switch>
            </div>
        </Router>
    );
};

export default App;
