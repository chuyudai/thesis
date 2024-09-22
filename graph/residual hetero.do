reg hgc m_hgc f_hgc phispanic pblack psex urban_at_14 rural_at_14 farm_at_14 age_stopped_living_w_parent i.reside_parent_type mother_work_1978 father_work_1978 cultural_influence teen_mom foreign_lang_child sibling sibling_school

predict residuals, residual

collapse (sd) residuals, by(hgc)

graph bar residuals, over(hgc, label(angle(0))) ///
    ytitle("Standard Deviation of Residuals", size(medium)) ///
    bar(1, color(midgreen)) ///
    blabel(bar, size(small) format(%9.2f) color(black)) ///
    title("Standard Deviation of Residuals by HGC Category", size(large)) ///
    yline(0, lwidth(medium) lcolor(gray)) ///
    legend(off) ///
    graphregion(color(white))
