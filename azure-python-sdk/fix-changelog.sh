#! /bin/bash

SPEC=$1
DIFFFILE=$(mktemp)

git diff ${SPEC} > ${DIFFFILE}
VERSION=$(grep -P '^\+Version:' ${DIFFFILE} | awk '{print $2}')
#tac ${DIFFFILE}
tac ${DIFFFILE} | grep -A2 '^ - Initial package.$' > ${DIFFFILE}.changes
REGEXP=$(grep -P '^\+\*\ ' ${DIFFFILE}.changes | sed -e 's/^\+\*/\\\*/g')
REPLACEMENT=$(grep -P '^\-\*\ ' ${DIFFFILE}.changes | sed -e 's/^\-\*/\\\*/g')
SED="sed -e \"s/^${REGEXP}$/${REPLACEMENT}/g\" ${SPEC}"
echo ${SED}
echo ${SED} | bash > ${SPEC}.new
if [ "${VERSION}" == "" ]; then
    echo "New release."
    rpmdev-bumpspec -c "- Rebuilt." ${SPEC}.new
else
    echo "New version."
    sed -i -e 's/Release:        1%{?dist}/Release:        0%{?dist}/g' ${SPEC}.new
    rpmdev-bumpspec -c "- Upgrade to version ${VERSION}." -n "${VERSION}" ${SPEC}.new
fi

cat ${SPEC}.new
echo
echo
echo
diff -u ${SPEC} ${SPEC}.new
mv ${SPEC} ${SPEC}.bak
mv ${SPEC}.new ${SPEC}

rm ${DIFFFILE} ${DIFFFILE}.changes
