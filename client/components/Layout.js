import React from "react";

import { Grid, Typography } from "@material-ui/core";

const Layout = () =>
{
	return(
		<Grid
			container
			justify={"center"}
			alignContent={"center"}
			alignItems={"center"}
			style={{height: "100vh"}}
			>
			<Grid item>
				<Typography variant={"h2"}>Hello World!</Typography>
			</Grid>
		</Grid>
	)
};

export default Layout;
