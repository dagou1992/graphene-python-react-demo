import Main from '../Main';
import { connect } from 'react-redux';
import * as mainAction from '../../redux/actions/mainAction';

const mapStateToProps = (state) => ({
    data: state.Main,
});

const mapDispatchToProps = {
    initPage: mainAction.initPage,
};

export default connect(mapStateToProps, mapDispatchToProps)(Main);