import {all, fork, put, takeEvery} from 'redux-saga/effects';

import * as mainAction from '../actions/mainAction';
import mainConstants from '../actions/constants/mainConstants';

function* initPage() {

}

function* watchInitPage() {
    yield takeEvery(mainConstants.INIT_PAGE, initPage);
}

export default function* watchRootSaga() {
    yield all([
        fork(watchInitPage),
    ])
}