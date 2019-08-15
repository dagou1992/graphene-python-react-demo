import React from 'react';
import { Route, Switch, Redirect, HashRouter } from 'react-router-dom';

import Main from '../components/containers/mainContainer';

export default (
    <Main>
        <HashRouter>
            <Switch>
                <Route exact path="/manage" component={() => <Redirect to="/manage"/> } />
            </Switch>
        </HashRouter>
    </Main>
);