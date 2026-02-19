import {React, useState, useEffect} from 'react'
import AxiosInstance from './Axios'
import MyPieChart from './charts/PieChart'
import MyChartBox from './charts/ChartBox'
import StoreIcon from '@mui/icons-material/Store';
import MyDonutChart from './charts/DonutChart'
import WcIcon from '@mui/icons-material/Wc';

const Dashboard1 = () => {

    const [myBranchData, setMyBranchData] = useState([])
    const [myGenderData, setMyGenderData] = useState([])

    const GetData = () => {
        AxiosInstance.get(`branchdata/`).then((res) => {
            setMyBranchData(res.data)
            })

        AxiosInstance.get(`genderdata/`).then((res) => {
            setMyGenderData(res.data)
            })
        }
    useEffect(() => {
        GetData()
        },[])

    return (
        <div>
            <MyChartBox
                icon1 = {<StoreIcon/>}
                title1 = {"Quantities per branch"}
                chart1 = {<MyPieChart
                            myData={myBranchData}
                            />}

                icon2 = {<WcIcon/>}
                title2 = {"Quantities per Gender"}
                chart2 = {<MyDonutChart
                            />}
            />


        </div>
        )
    }

export default Dashboard1