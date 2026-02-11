-- 1. Which cities have the most highly-rated businesses?
SELECT 
    city, 
    COUNT(*) as business_count, 
    AVG(stars) as avg_rating
FROM YELP_BUSINESS
GROUP BY city
HAVING business_count > 100
ORDER BY avg_rating DESC
LIMIT 10;

-- 2. Analyze review sentiment by looking for keywords
SELECT 
    stars,
    COUNT(*) as review_count
FROM YELP_REVIEWS
WHERE text LIKE '%excellent%' OR text LIKE '%amazing%'
GROUP BY stars;
