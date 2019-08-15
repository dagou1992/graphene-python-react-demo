import * as React from 'react';
import { HashRouter, Route, Switch, Redirect } from 'react-router-dom';

import mainRouter from './mainRouter';

const Router = () => {
    return (
        <HashRouter>
            <Switch>
                <Route path="/" component={() => mainRouter} />
                <Redirect to='/' />
            </Switch>
        </HashRouter>
    );
};

export default Router;