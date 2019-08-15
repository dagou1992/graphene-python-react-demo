import mainConstants from '../actions/constants/mainConstants';

const initialState = {
    dataSource: [],
};

const mainReducer = (state = initialState, action) => {
    switch (action.type) {
        case mainConstants.INIT_PAGE:
            return initialState;

        default:
            return state;
    }
};

export default mainReducer;