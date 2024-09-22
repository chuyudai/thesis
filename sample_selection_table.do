local vars sibling sibling_school dad_age mom_age afqt ever_married st_marry_age desire_child_ abort_

foreach var of local vars {
    ttest `var', by(teen_mom)
}
