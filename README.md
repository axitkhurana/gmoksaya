## gmoksaya

gmoksaya is a client library for Sugarlabs' project sharing website making it easier to integrate in Glib2 code.

### Example

    from gmoksaya.projects import Project

    project = projects.Project()
    project.connect('completed', __phase1_completed_cb)
    project.connect('failed', __phase1_failed_cb)
    project.create(2, 'test_title', 'test_description', 'test_file1',
                   'test_file2.jpg')

For more examples, check the tests folder.

### Dependencies

* grestful [https://github.com/tchx84/grestful]
