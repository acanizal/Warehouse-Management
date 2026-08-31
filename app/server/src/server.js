const express = require("express");
const cors = require("cors");
const pool = require("./db/db");


//require("dotenv").config();

const app = express();

app.use(cors());
app.use(express.json());
/*
app.get("/api/health", (req,res) => {
    res.json({message: "API is working"});

});
*/
app.get("/api/users", async (req,res) => {
    try {
        const result = await pool.query(
            "SELECT * FROM pruhart.orders"
        );
        res.json(result.rows);

    } catch (error) {
        console.error(error);
        res.status(500).json({
            error: "Database error"
        });
    }
});

app.listen(5000, () => {
    console.log("Server running on port 5000")
})
