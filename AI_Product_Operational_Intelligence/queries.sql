SELECT AVG(session_length) FROM dataset;

SELECT COUNT(*) FROM dataset WHERE conversion = 1;

SELECT SUM(revenue) FROM dataset;

SELECT retention_flag, COUNT(*) FROM dataset GROUP BY retention_flag;

