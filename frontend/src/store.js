import { createStore, applyMiddleware } from 'redux';
import reducer from './redux/reducers/';
import createSagaMiddleware from 'redux-saga';
import logger from 'redux-logger';
import rootSaga from './redux/sagas/';

const sagaMiddleware = createSagaMiddleware();

const middleware = [sagaMiddleware, logger];
const store = createStore(reducer, applyMiddleware(...middleware));

sagaMiddleware.run(rootSaga);

export default store;