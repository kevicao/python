val df=spark.sql(s"""
    with data as (
    SELECT 
        marketplace_id
        , http_request_id
        , child_http_request_id
        , search_query
        , '1' as impr
        , customer_id
        , cpc
        , case when cpc > 10 then 10 else cpc end as capped_cpc
        , ramp_score
        , CAST((CASE WHEN clicks_count > inv_clicks_count THEN 1 ELSE 0 END) AS BIGINT) AS clicks    
        , page_asin

        , case 
            when widget_name in ('sp_atf_browse', 'sp_btf_browse' 'sp_mtf_browse', 'sp_phone_browse_atf', 'sp_phone_browse_btf', 'sp_phone_browse_mtf', 'sp_phoneapp_browse', 'sp_phoneapp_browse_atf', 'sp_phoneapp_browse_mtf') then 'browse'
            when widget_name in ("sp_atf", "sp_btf", "sp_mtf", "sp_atf_next", 
                "sp_phoneapp_search_atf", "sp_phoneapp_search", "sp_phoneapp_search_mtf", 
                "sp_phone_search_atf", "sp_phone_search_btf", "sp_phone_search_mtf") then 'search'
        end as widget_group

    FROM spektr_ach.d_sp_ach_smml
    WHERE inv_impressions_count = 0
            AND spektr_date = '2021-03-20'
            and widget_name in ("sp_atf", "sp_btf", "sp_mtf", "sp_atf_next", 
                "sp_phoneapp_search_atf", "sp_phoneapp_search", "sp_phoneapp_search_mtf", 
                "sp_phone_search_atf", "sp_phone_search_btf", "sp_phone_search_mtf", 'sp_atf_browse', 'sp_btf_browse' 'sp_mtf_browse', 'sp_phone_browse_atf', 'sp_phone_browse_btf', 'sp_phone_browse_mtf', 'sp_phoneapp_browse', 'sp_phoneapp_browse_atf', 'sp_phoneapp_browse_mtf')
    )

    select *
        , cpc*clicks as rev
        , capped_cpc*clicks as capped_rev
    from data

""") 


df.groupBy("marketplace_id","widget_group").agg(
    sum("impr").alias("imprs")
    , sum("rev").alias("revenue")
).show(1000,false)