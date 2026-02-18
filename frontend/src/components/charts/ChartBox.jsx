import * as React from 'react';
import { Grid, Box } from '@mui/material';

export default function MyChartBox(props) {
  const {icon1, title1, chart1} = props
  return (
    <>
        <Grid container
            sx={{width:'100%', display: 'flex', minHeight:'200px', boxShadow: 3, justifyContent: 'space-evenly'}}
        >
            <Grid
                item xs={12} sm={12} md={6} lg={4}
                sx={{minHeight: '200px', padding: '20px', backgroundColor:'red'}}
            >
                <Box>
                    <Box>{icon1}</Box>
                    <Box>{title1}</Box>
                </Box>

                <Box>{chart1}</Box>

            </Grid>

            <Grid
                item xs={12} sm={12} md={6} lg={4}
                sx={{minHeight: '200px', padding: '20px', backgroundColor:'blue'}}
            >


            </Grid>

            <Grid
                item xs={12} sm={12} md={6} lg={4}
                sx={{minHeight: '200px', padding: '20px', backgroundColor:'purple'}}
            >


            </Grid>
        </Grid>
    </>
  );
}
