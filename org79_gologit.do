gen sampleid = 1 if 1 < hgc & hgc < 9
drop if sampleid != 1


gologit2 hgc teen_mom black female f_hgc m_hgc dad_age mom_age sibling sibling_school cultural_influence urban_at_14 age_stopped_living_w_parent mother_work_1978 father_work_1978, pl(sibling_school sibling urban_at_14 father_work_1978)

gologit2 hgc teen_mom##female black f_hgc m_hgc dad_age mom_age sibling sibling_school cultural_influence urban_at_14 age_stopped_living_w_parent mother_work_1978 father_work_1978




// gen YAsampleid = 1 if 1 < hgc_ya & hgc_ya < 9
// drop if YAsampleid != 1
// gologit2 hgc_ya teen_mom_ya teen_mom m_hgc_ya f_hgc m_hgc momexpectyos cfemale1 pblack avg_fam_inc behaveproblemindexpercentilescor everrepeatedagrade desire_child_ married_age, pl(teen_mom) 
