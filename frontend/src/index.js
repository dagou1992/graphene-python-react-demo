import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import ApolloClient from 'apollo-boost';
import { ApolloProvider } from '@apollo/react-hooks';

import store from './store'
import Router from './router';

const client = new ApolloClient({
    uri: "http://192.168.3.110:5000/graphql"
});

ReactDOM.render(
    <Provider store={store}>
        <ApolloProvider client={client}>
            <Router />
        </ApolloProvider>
    </Provider>,
    document.getElementById('root'));
