import {React, useState, useEffect} from 'react'
import AxiosInstance from './Axios'
import MyPieChart from './charts/PieChart'
import MyChartBox from './charts/ChartBox'
import StoreIcon from '@mui/icons-material/Store';

const Dashboard1 = () => {

    const [myBranchData, setMyBranchData] = useState([])

    const GetData = () => {
        AxiosInstance.get(`branchdata/`).then((res) => {
            setMyBranchData(res.data)
            })
        }
    useEffect(() => {
        GetData()
        },[])

    return (
        <div>
            <MyChartBox
                icon1 = {<StoreIcon/>}
                title1 = {"This is my title"}
                chart1 = {<MyPieChart
                            myData={myBranchData}
                            />}
            />


        </div>
        )
    }

export default Dashboard1