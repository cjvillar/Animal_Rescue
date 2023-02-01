import {Route ,Navigate, Routes} from 'react-router-dom'

const PrivateRoute = ({children, ...rest}) =>
{
const authenticated = false
return(
    <Routes path="">
        <Route {...rest}>{!authenticated ? <Navigate to='/LoginPage' replace={true} />  : children}</Route>
    </Routes>
) 
}
export default PrivateRoute